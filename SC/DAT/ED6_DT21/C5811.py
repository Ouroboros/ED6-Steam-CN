import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5811_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5811   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5811.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x8C7
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
        ScenaActorData(
            triggerX            = -11900,
            triggerZ            = 0,
            triggerY            = -5480,
            triggerRange        = 1500,
            actorX              = -11900,
            actorZ              = 1000,
            actorY              = -5480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4730,
            triggerZ            = 0,
            triggerY            = 12330,
            triggerRange        = 1000,
            actorX              = 5090,
            actorZ              = 1000,
            actorY              = 12940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5410,
            triggerZ            = 0,
            triggerY            = 12060,
            triggerRange        = 1000,
            actorX              = -5740,
            actorZ              = 1000,
            actorY              = 12680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5160,
            triggerZ            = 0,
            triggerY            = -11960,
            triggerRange        = 1000,
            actorX              = 5370,
            actorZ              = 1000,
            actorY              = -12630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x138
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x139
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0474, 0, 0x23A0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14B',
    )

    OP_6F(0x0002, 0)

    Jump('loc_152')

    def _loc_14B(): pass

    label('loc_14B')

    OP_6F(0x0002, 60)

    def _loc_152(): pass

    label('loc_152')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0474, 1, 0x23A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_164',
    )

    OP_6F(0x0003, 0)

    Jump('loc_16B')

    def _loc_164(): pass

    label('loc_164')

    OP_6F(0x0003, 60)

    def _loc_16B(): pass

    label('loc_16B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0474, 2, 0x23A2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17D',
    )

    OP_6F(0x0004, 0)

    Jump('loc_184')

    def _loc_17D(): pass

    label('loc_17D')

    OP_6F(0x0004, 60)

    def _loc_184(): pass

    label('loc_184')

    Return()

# id: 0x0002 offset: 0x185
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xBA, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0474, 0, 0x23A0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_286',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000001E)
    OP_73(0x0002)
    OP_6F(0x0002, 30)
    AddItem(ItemTable['魔兽羽翼'], 10)
    AddItem(ItemTable['魔兽之骨'], 10)
    AddItem(ItemTable['魔兽鸟肉'], 10)
    AddItem(ItemTable['魔兽鸟蛋'], 10)
    AddItem(ItemTable['魔兽之种'], 10)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽羽翼　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽之骨　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽鸟肉　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽鸟蛋　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽之种　　　×１０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x23A0)

    Jump('loc_2A0')

    def _loc_286(): pass

    label('loc_286')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_2A0(): pass

    label('loc_2A0')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x2B2
@scena.Code('func_03_2B2')
def func_03_2B2():
    UnlockAchievement(0x02, 0xBB, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0474, 1, 0x23A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B3',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000001E)
    OP_73(0x0003)
    OP_6F(0x0003, 30)
    AddItem(ItemTable['魔兽之角'], 10)
    AddItem(ItemTable['魔兽尾巴'], 10)
    AddItem(ItemTable['魔兽之牙'], 10)
    AddItem(ItemTable['魔兽甲壳'], 10)
    AddItem(ItemTable['魔兽之肉'], 10)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽之角　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽尾巴　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽之牙　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽甲壳　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽之肉　　　×１０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x23A1)

    Jump('loc_3CD')

    def _loc_3B3(): pass

    label('loc_3B3')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_3CD(): pass

    label('loc_3CD')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x3DF
@scena.Code('func_04_3DF')
def func_04_3DF():
    UnlockAchievement(0x02, 0xBC, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0474, 2, 0x23A2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C0',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000001E)
    OP_73(0x0004)
    OP_6F(0x0004, 30)
    AddItem(ItemTable['魔兽眼珠'], 10)
    AddItem(ItemTable['魔兽鱼肉'], 10)
    AddItem(ItemTable['魔兽明胶'], 10)
    AddItem(ItemTable['魔兽鱼卵'], 10)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽眼珠　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽鱼肉　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽明胶　　　×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#20I魔兽鱼卵　　　×１０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x23A2)

    Jump('loc_4DA')

    def _loc_4C0(): pass

    label('loc_4C0')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4DA(): pass

    label('loc_4DA')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x4EC
@scena.Code('func_05_4EC')
def func_05_4EC():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在由于系统故障的影响，\n',
            '可选择项目受到了一定的限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        40,
        90,
        1,
        (
            TXT(0x00, '【领取随身行李】\n'),
            TXT(0x01, '【放弃使用】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5A1'),
        (0x00000001, 'loc_893'),
        (-1, 'loc_896'),
    )

    def _loc_5A1(): pass

    label('loc_5A1')

    If(
        (
            (Expr.Eval, "OP_40(0x0417, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0456, 0, 0x22B0)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_642',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S开始核对………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S………………侦测不到数据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在这里没有\n',
            '您所寄放的行李。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_890')

    def _loc_642(): pass

    label('loc_642')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S开始核对…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S………确认特定周波模型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S确认为已登录的受托人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S保管物＃R-8834-0033开始转送。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S数据接收中…………２０％………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S……４０％……………６０％………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S……８０％……………转送完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_5F(0x0000)
    Sleep(200)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶Ｚ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶Ｚ'], 1)

    ChrTalk(
        0x0101,
        (
            '#0010391401V#1004F这、这个\n',
            '是资料水晶吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391402V好像是从什么地方\n',
            '运送过来的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391403V#1042F看来是对我们身上\n',
            '携带的物品产生了反应呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391404V#1040F如果交给拉赛尔博士，\n',
            '说不定就能明白它的内容了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22B0)

    def _loc_890(): pass

    label('loc_890')

    Jump('loc_896')

    def _loc_893(): pass

    label('loc_893')

    Jump('loc_896')

    def _loc_896(): pass

    label('loc_896')

    OP_5F(0x0000)
    OP_56(0x00)
    Sleep(200)

    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
