import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1300_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1300_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x9F2
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetChrPos(0x0000, -39200, 0, 31000, 0)
    SetChrPos(0x0001, -39200, 0, 32200, 0)
    SetChrPos(0x0002, -39200, 0, 33400, 0)
    SetChrPos(0x000A, -39200, 0, 34600, 0)
    CreateThread(0x0000, 0x01, 0x01, 0x0001)
    CreateThread(0x0001, 0x01, 0x01, 0x0002)
    CreateThread(0x0002, 0x01, 0x01, 0x0003)
    CreateThread(0x000A, 0x01, 0x01, 0x0004)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    @scena.Lambda('lambda_00DD')
    def lambda_00DD():
        OP_6C(225000, 8000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_00DD)

    @scena.Lambda('lambda_00ED')
    def lambda_00ED():
        CameraSetDistance(2800, 8000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_00ED)

    CameraMove(-50000, 0, 6500, 8000)
    OP_A5(0x0001)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Fade(1000)
    SetChrPos(0x0101, -51000, 0, 18400, 180)
    SetChrPos(0x0102, -50000, 0, 20000, 180)
    SetChrPos(0x0103, -50000, 0, 17200, 180)
    SetChrPos(0x000A, -48500, 0, 21500, 180)
    OP_69(0x0101, 0)

    @scena.Lambda('lambda_016D')
    def lambda_016D():
        ChrWalkTo(0x0101, -51000, 0, 17400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_016D)

    @scena.Lambda('lambda_0188')
    def lambda_0188():
        ChrWalkTo(0x0102, -50000, 0, 19000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0188)

    @scena.Lambda('lambda_01A3')
    def lambda_01A3():
        ChrWalkTo(0x0103, -50000, 0, 15800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_01A3)

    @scena.Lambda('lambda_01BE')
    def lambda_01BE():
        ChrWalkTo(0x000A, -48500, 0, 17400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_01BE)

    @scena.Lambda('lambda_01D9')
    def lambda_01D9():
        CameraMove(-50000, 0, 17400, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_01D9)

    Sleep(1000)

    Sleep(2000)

    ChrTalk(
        0x000A,
        (
            '#1370151269V哈，总算到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151270V#007F呼，\n',
            '真是不容易啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151271V#010F现在终于可以放松一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x000A, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151272V#020F从卢安来接你的游击士\n',
            '应该很快就会到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    SetChrDirection(0x0103, 180, 400)
    Sleep(800)

    ChrTalk(
        0x0103,
        (
            '#0030151273V#020F……看吧，\n',
            '刚说着他就来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000B, -50000, 500, 8700, 0)
    ClearChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_0322')
    def lambda_0322():
        ChrTurnDirection(0x0101, 0x000B, 400)
        Yield()

        Jump('lambda_0322')

    DispatchAsync2(0x0101, 0x0001, lambda_0322)

    @scena.Lambda('lambda_0333')
    def lambda_0333():
        ChrTurnDirection(0x0102, 0x000B, 400)
        Yield()

        Jump('lambda_0333')

    DispatchAsync2(0x0102, 0x0001, lambda_0333)

    @scena.Lambda('lambda_0344')
    def lambda_0344():
        ChrTurnDirection(0x0103, 0x000B, 400)
        Yield()

        Jump('lambda_0344')

    DispatchAsync2(0x0103, 0x0001, lambda_0344)

    @scena.Lambda('lambda_0355')
    def lambda_0355():
        ChrTurnDirection(0x000A, 0x000B, 400)
        Yield()

        Jump('lambda_0355')

    DispatchAsync2(0x000A, 0x0001, lambda_0355)

    OP_70(0x0001, 100)
    OP_73(0x0001)
    OP_6F(0x0001, 100)
    OP_70(0x0001, 0)
    ChrWalkTo(0x000B, -50000, 500, 13200, 3000, 0x00)
    ChrWalkTo(0x000B, -48400, 500, 15800, 3000, 0x00)
    ChrTurnDirection(0x000B, 0x0103, 400)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Sleep(800)

    ChrTalk(
        0x000B,
        (
            '#1380151274V辛苦你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1380151275V我是卢安支部所属的\n',
            '准游击士梅尔茨！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151276V#020F你也辛苦了。\n',
            '这边这位就是委托人哈尔德先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151277V待会儿就拜托你\n',
            '把他护送到卢安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1380151278V明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#1380151279V请您多多指教！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151280V你、你还真是\n',
            '精神抖擞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151281V总之就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#1370151282V刚才多谢\n',
            '你们三位的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151283V#001F保重哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000A, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151284V#010F工作方面也请加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x000A,
        (
            '#1370151285V哈哈，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151286V虽然可能已经迟到了，\n',
            '不过我会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0103, 400)

    ChrTalk(
        0x000B,
        (
            '#1380151287V那么我们就失陪了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000B, 0x01, 0x01, 0x0005)
    CreateThread(0x000A, 0x01, 0x01, 0x0006)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    @scena.Lambda('lambda_05EF')
    def lambda_05EF():
        ChrTurnDirection(0x0101, 0x000A, 400)
        Yield()

        Jump('lambda_05EF')

    DispatchAsync2(0x0101, 0x0001, lambda_05EF)

    @scena.Lambda('lambda_0600')
    def lambda_0600():
        ChrTurnDirection(0x0102, 0x000A, 400)
        Yield()

        Jump('lambda_0600')

    DispatchAsync2(0x0102, 0x0001, lambda_0600)

    @scena.Lambda('lambda_0611')
    def lambda_0611():
        ChrTurnDirection(0x0103, 0x000A, 400)
        Yield()

        Jump('lambda_0611')

    DispatchAsync2(0x0103, 0x0001, lambda_0611)

    OP_A5(0x0005)
    OP_A5(0x0007)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    OP_6F(0x0001, 100)
    OP_70(0x0001, 0)
    OP_73(0x0001)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010151288V#004F竟然会有这么精神抖擞的人啊～\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151289V#010F是个准游击士呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151290V和我们一样，\n',
            '好像也正在支部进行实习……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0102, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151291V#020F嗯，不止是你们，\n',
            '很多人都想成为优秀的游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151292V所以说，为了成为正游击士，\n',
            '你们更要拼命努力才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151293V#002F嗯～\n',
            '我也要加倍努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151294V#010F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151295V我们总是要依靠雪拉姐姐，\n',
            '还真是有点过意不去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151296V#021F呵呵，看来受到了鞭策呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151297V那么，\n',
            '我们回协会汇报工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0010, 0x04, 0x10)
    OP_28(0x0010, 0x03, 0x08)
    OP_28(0x0010, 0x01, 0x0020)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【护卫委托】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearMapFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x87E
@scena.Code('Init')
def Init():
    OP_A6(0x0001)
    ChrWalkTo(0x0000, -50000, 0, 18000, 2000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0002 offset: 0x899
@scena.Code('ReInit')
def ReInit():
    OP_A6(0x0002)
    ChrWalkTo(0x0001, -39200, 0, 31000, 2000, 0x00)
    ChrWalkTo(0x0001, -50000, 0, 18000, 2000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x0003 offset: 0x8C8
@scena.Code('func_03_8C8')
def func_03_8C8():
    OP_A6(0x0003)
    ChrWalkTo(0x0002, -39200, 0, 31000, 2000, 0x00)
    ChrWalkTo(0x0002, -50000, 0, 18000, 2000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x0004 offset: 0x8F7
@scena.Code('func_04_8F7')
def func_04_8F7():
    OP_A6(0x0004)
    ChrWalkTo(0x000A, -39200, 0, 31000, 2000, 0x00)
    ChrWalkTo(0x000A, -50000, 0, 18000, 2000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

# id: 0x0005 offset: 0x926
@scena.Code('func_05_926')
def func_05_926():
    OP_A6(0x0005)
    ChrWalkTo(0x000B, -50000, 500, 13200, 2000, 0x00)
    ChrWalkTo(0x000B, -50000, 500, 10458, 2000, 0x00)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 100)
    OP_73(0x0001)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrWalkTo(0x000B, -50000, 500, 6700, 2000, 0x00)
    SetChrFlags(0x000B, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Return()

# id: 0x0006 offset: 0x982
@scena.Code('func_06_982')
def func_06_982():
    OP_A6(0x0006)
    ChrWalkTo(0x000A, -48400, 500, 15800, 2000, 0x00)
    ChrWalkTo(0x000A, -50000, 500, 13200, 2000, 0x00)
    ChrWalkTo(0x000A, -50000, 500, 11400, 1000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    OP_A6(0x0007)
    ChrWalkTo(0x000A, -50000, 500, 8700, 2000, 0x00)
    SetChrFlags(0x000A, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
