import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4100_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4100_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4100.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T4100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x517
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    EventBegin(0x00)
    Fade(1000)
    OP_6D(-5500, 0, -40280, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -190, 0, -40890, 180)
    SetChrPos(0x0105, -1400, 0, -40150, 180)
    SetChrPos(0x0104, 620, 0, -40140, 180)
    SetChrPos(0x0108, -570, 0, -39260, 180)
    SetChrPos(0x0028, -2070, 0, -5120, 180)
    SetChrPos(0x0029, 3520, 0, 10640, 180)
    OP_4A(0x0028, 255)
    OP_4A(0x0029, 255)
    OP_0D()
    Sleep(2000)

    @scena.Lambda('lambda_0166')
    def lambda_0166():
        OP_6D(-1400, 0, -41100, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0166)

    @scena.Lambda('lambda_017E')
    def lambda_017E():
        OP_67(0, 6940, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_017E)

    @scena.Lambda('lambda_0196')
    def lambda_0196():
        OP_6B(2800, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0196)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010460336V#1015F『留在地上的象征』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460337V这个白隼的雕像\n',
            '感觉是挺可疑的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460338V#070F唔，确实是\n',
            '作为利贝尔象征的鸟嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460339V#040F那就调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0101, -190, 0, -42110, 1000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查铁栅栏的底部\n',
            '发现贴着卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    OP_AD(0x00240093, 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170460340V　　第三把钥匙在异国之馆中。　\n',
            '　看看『苍骑士的决心』。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_8C(0x0101, 0, 400)

    @scena.Lambda('lambda_033A')
    def lambda_033A():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_033A')

    DispatchAsync2(0x0105, 0x0002, lambda_033A)

    @scena.Lambda('lambda_034B')
    def lambda_034B():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_034B')

    DispatchAsync2(0x0104, 0x0002, lambda_034B)

    OP_8E(0x0101, -190, 0, -41390, 1000, 0x00)
    TerminateThread(0x0105, 0x02)
    TerminateThread(0x0104, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010460341V#1006F好，找对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460342V#1015F不过『苍之骑士』\n',
            '是指什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460343V是亲卫队的队员们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460344V#040F啊啊……\n',
            '确实是青色军服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460345V#030F不，说是『异国之馆』\n',
            '跟亲卫队不搭边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460346V#035F怎么说都太不够华丽了\n',
            '应该想想其他可能性吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460347V#1019F是，是这样吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460348V#1015F（嗯，既然是同类说的话\n',
            '最好是遵从忠告……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C4, 0x01, 0x0010)
    OP_28(0x00C4, 0x01, 0x0020)
    OP_64(0x07, 0x0001)
    OP_4B(0x0028, 255)
    OP_4B(0x0029, 255)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
